import hashlib

def double_sha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()

def txid_to_internal_bytes(txid_hex):
    return bytes.fromhex(txid_hex)[::-1]

def internal_bytes_to_hex(b):
    return b[::-1].hex()

def merkle_parent(left, right):
    return double_sha256(left + right)

def build_merkle_tree(txids_hex):
    level = [txid_to_internal_bytes(t) for t in txids_hex]
    levels = [level]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level = level + [level[-1]]
        next_level = []
        for i in range(0, len(level), 2):
            next_level.append(merkle_parent(level[i], level[i + 1]))
        levels.append(next_level)
        level = next_level
    return levels, level[0]

if __name__ == "__main__":
    txids = [
        "d5aa81e54bcbcc7ea312f3be3ad6a4046a1dcfe9643904180252a7f5818d26b1",
        "9970a8292c62998c088e87f73a7a21da64191022688d92179a47d8911507912e",
        "d73ce1e0d503b2207cf4919e227448712242300fb028f841ec8225c855cafa61",
        "ee75f031e75f6972b552dba70f1a13e5fc71f5b37829ec59ed96cec70a1d0445",
    ]

    print("=== Leaf transactions ===")
    for i, t in enumerate(txids, 1):
        print(f"Tx{chr(64 + i)}: {t}")

    levels, root = build_merkle_tree(txids)

    print("\n=== Tree levels (bottom to top) ===")
    for depth, level in enumerate(levels):
        print(f"\nLevel {depth} ({len(level)} node(s)):")
        for node in level:
            print(f"  {internal_bytes_to_hex(node)}")

    print("\n=== Result ===")
    print(f"Computed Merkle Root: {internal_bytes_to_hex(root)}")
    print("\nNote: this will NOT match block 402090's real merkle root")
    print("(71643a766c206772c0ef1bca9adf75fc66b1738ee0dd6fd56aee4d20a67fa85c)")
    print("because the real block has 192 transactions, not 4. This script")
    print("demonstrates the correct pairwise-hashing algorithm on a subset.")
