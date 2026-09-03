import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

def short(h, n=10):
    return h[:n] + "..."

# Real values from merkle_tree.py output
root      = "31630b5976fafe4866f6e7ce545c535e2f5a331f08e4de9d7b118a7c43978cfe"
hash_ab   = "fbf2db5edc44901f53aa84dac988b63ebfb77b50d1c578dcb8639a23582f6cb8"
hash_cd   = "39d48363fa7af318b7832b3ab8ea73b0be35618c11e3ab06f06f579e55c81ec6"
txa = "d5aa81e54bcbcc7ea312f3be3ad6a4046a1dcfe9643904180252a7f5818d26b1"
txb = "9970a8292c62998c088e87f73a7a21da64191022688d92179a47d8911507912e"
txc = "d73ce1e0d503b2207cf4919e227448712242300fb028f841ec8225c855cafa61"
txd = "ee75f031e75f6972b552dba70f1a13e5fc71f5b37829ec59ed96cec70a1d0445"

def box(x, y, label, value, color="#dbeafe"):
    ax.text(x, y, f"{label}\n{short(value)}", ha='center', va='center',
             fontsize=9, bbox=dict(boxstyle="round,pad=0.5", facecolor=color, edgecolor="black"))

# Level 2 - Root
box(5, 7, "Merkle Root", root, "#fca5a5")

# Level 1
box(3, 5, "Hash(AB)", hash_ab, "#fde68a")
box(7, 5, "Hash(CD)", hash_cd, "#fde68a")

# Level 0 - Leaves
box(1.5, 3, "TxA (coinbase)", txa, "#bbf7d0")
box(4.5, 3, "TxB", txb, "#bbf7d0")
box(5.5, 3, "TxC", txc, "#bbf7d0")
box(8.5, 3, "TxD", txd, "#bbf7d0")

# Connecting lines
ax.plot([5, 3], [6.5, 5.5], 'k-', lw=1)
ax.plot([5, 7], [6.5, 5.5], 'k-', lw=1)
ax.plot([3, 1.5], [4.5, 3.5], 'k-', lw=1)
ax.plot([3, 4.5], [4.5, 3.5], 'k-', lw=1)
ax.plot([7, 5.5], [4.5, 3.5], 'k-', lw=1)
ax.plot([7, 8.5], [4.5, 3.5], 'k-', lw=1)

ax.set_title("Merkle Tree — Block 402090 (first 4 transactions)", fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig("merkle-tree-diagram.png", dpi=150, bbox_inches='tight')
print("Saved merkle-tree-diagram.png")
