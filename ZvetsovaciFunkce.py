def ZvetsiTotoSlovo(slovo):
    if len(slovo) > 1:
        return slovo[0].upper() + slovo[1::]
    else:
        return slovo