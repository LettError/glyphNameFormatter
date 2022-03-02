

def process(self):
    self.edit("MATHEMATICAL")
    self.replace("PARENTHESIS", "paren")
    self.edit("AND WITH DOT", "andwithdot")
    self.edit("FLATTENED", "flat")
    self.edit("CONCAVE-SIDED DIAMOND", "convavediamond")
    self.edit("LEFTWARDS", "left")
    self.edit("RIGHTWARDS", "right")
    self.edit("LEFT AND RIGHT", "leftright")
    self.edit("UPWARDS", "up")
    self.edit("UPPER", "up")
    self.edit("TORTOISE SHELL", "shell")
    self.edit("S-SHAPED", "sshape")
    parts = [
        "WHITE", "ANGLE", "SQUARE", "DIAMOND", "FULL",
        "REVERSE", "SUPERSET", "PRECEDING",
        ]
    for part in parts:
        self.edit(part, part.lower())

    self.edit("AND")
    self.processAs("Mathematical Operators")


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Miscellaneous Mathematical Symbols-A")
