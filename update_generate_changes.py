import polib
import sys
import csv


def load_translations(po):
    translations = {}
    for entry in po:
        if entry.obsolete:
            continue
        if entry.msgid_with_context in translations:
            print(entry)
        translations[entry.msgid_with_context] = entry
    return translations


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(
            "{} OLD_PRETIX.po NEW_PRETIX.po OLD_JH.po CHANGES.csv".format(sys.argv[0])
        )
        sys.exit(1)
    with open(sys.argv[4], "w") as f:
        writer = csv.DictWriter(
            f, ["context", "msgid", "pretix_old", "pretix_new", "jh_old", "jh_new"]
        )
        writer.writeheader()
        old_pretix_po = polib.pofile(sys.argv[1])
        new_pretix_po = polib.pofile(sys.argv[2])
        jh_po = polib.pofile(sys.argv[3])
        jh_translation = load_translations(jh_po)
        old_pretix_translation = load_translations(old_pretix_po)
        new_pretix_translation = load_translations(new_pretix_po)
        for msgid, entry in new_pretix_translation.items():
            # new texts
            if msgid not in old_pretix_translation or msgid not in jh_translation:
                old_text = ""
                if msgid in old_pretix_translation:
                    old_text = old_pretix_translation[msgid].msgstr
                jh_text = ""
                if msgid in jh_translation:
                    jh_text = jh_translation[msgid].msgstr
                writer.writerow(
                    {
                        "context": entry.msgctxt,
                        "msgid": entry.msgid,
                        "pretix_old": old_text,
                        "pretix_new": entry.msgstr,
                        "jh_old": jh_text,
                        "jh_new": "HIHI FIND ME",
                    }
                )
            # text that changes
            if msgid in old_pretix_translation:
                if (
                    new_pretix_translation[msgid].msgstr
                    != old_pretix_translation[msgid].msgstr
                ):
                    old_text = old_pretix_translation[msgid].msgstr
                    jh_text = ""
                    if msgid in jh_translation:
                        jh_text = jh_translation[msgid].msgstr
                    writer.writerow(
                        {
                            "context": entry.msgctxt,
                            "msgid": entry.msgid,
                            "pretix_old": old_text,
                            "pretix_new": entry.msgstr,
                            "jh_old": jh_text,
                            "jh_new": "HIHI FIND ME",
                        }
                    )
