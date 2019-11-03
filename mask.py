def mask(txt):
    if len(txt) > 4:
        masked = len(txt) - 4
        show = txt[masked:len(txt)]
        return ("#" * masked) + show
    return txt
