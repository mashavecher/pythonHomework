"""
one-letter codes for degenerate bases are determined
by the International Union of Biochemistry (IUB), based on base properties.
"""

IUB_TO_DEG_F = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    'B': '[GCA]',
    'D': '[TCA]',
    'H': '[TGA]',
    'K': '[CA]',
    'M': '[TG]',
    'R': '[TC]',
    'S': '[GC]',
    'V': '[TGC]',
    'W': '[TA]',
    'Y': '[GA]',
}

IUB_TO_DEG_R = {
    'A': 'A',
    'T': 'T',
    'C': 'C',
    'G': 'G',
    'B': '[CGT]',
    'D': '[AGT]',
    'H': '[ACT]',
    'K': '[GT]',
    'M': '[AC]',
    'R': '[AG]',
    'S': '[CG]',
    'V': '[ACG]',
    'W': '[AT]',
    'Y': '[CT]',
}
