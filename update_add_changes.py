import polib
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print(
            "{} OLD_PRETIX.po NEW_PRETIX.po OLD_JH.po CHANGES_TRANSLATED.csv NEW_JH.po".format(sys.argv[0])
        )
        sys.exit(1)
    with open(sys.argv[4], "r") as f:
        reader = csv.DictReader(f)
        old_pretix_po = polib.pofile(sys.argv[1])
        new_pretix_po = polib.pofile(sys.argv[2])
        old_jh_po = polib.pofile(sys.argv[3])
        # we base the new jh po on the new_pretix_po
        new_jh_po = polib.pofile(sys.argv[2])
        for row in reader:
            # Safety check
            old_pretix_entry = old_pretix_po.find(row["msgid"],msgctxt=row["context"] if row["context"] else False)
            if row["pretix_old"] and not old_pretix_entry:
                print("Error: according to the changes.csv, pretix_old had a translation, but I could not find it")
                sys.exit(1)
            new_pretix_entry = new_pretix_po.find(row["msgid"],msgctxt=row["context"] if row["context"] else False)
            if row["pretix_new"] and not new_pretix_entry:
                print("Error: according to the changes.csv, pretix_new had a translation, but I could not find it")
                sys.exit(1)
            old_jh_entry = old_jh_po.find(row["msgid"],msgctxt=row["context"] if row["context"] else False)
            if row["jh_old"] and not old_jh_entry:
                print("Error: according to the changes.csv, jh_old had a translation, but I could not find it")
                sys.exit(1)
            new_jh_entry = new_jh_po.find(row["msgid"],msgctxt=row["context"] if row["context"] else False)
            if not new_jh_entry:
                print("Could not find translation in new files")
            new_jh_entry.msgstr = row["jh_new"]
        new_jh_po.metadata['Language-Team'] = "Jugend hackt Team based on " + new_jh_po.metadata['Language-Team']
        new_jh_po.metadata["Last-Translator"] = "Jugend hackt Team"
        new_jh_po.save(sys.argv[5])
