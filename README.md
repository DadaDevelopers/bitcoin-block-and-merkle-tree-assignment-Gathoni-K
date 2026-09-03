# Bitcoin Block and Merkle Tree Assignment

## Overview

This submission covers block inspection and Merkle tree construction using real Bitcoin mainnet data (Block 402090).

## Task 1: Block Inspection

See `block-inspection.md` for full details. Summary:

- Block Height: 402090
- Block Hash: 000000000000000003044f84e17656dc826a8f4d1ff4316d1a20877263c9b8d4
- Previous Block Hash: 00000000000000000283e0c86c702a017212b69a798e19ac664dcdaec24660c8
- Merkle Root: 71643a766c206772c0ef1bca9adf75fc66b1738ee0dd6fd56aee4d20a67fa85c
- Number of Transactions: 192

Data sourced from [mempool.space](https://mempool.space/block/402090).

## Task 2: Merkle Tree Visualization

Built a 4-leaf Merkle tree from the first 4 real transaction hashes in block 402090 (coinbase + 3 transactions), using Python and double-SHA256 hashing — Bitcoin's standard hashing method.

**Process:**
1. Took 4 real txids from the block (`code/merkle_tree.py`).
2. Reversed each txid's byte order (Bitcoin stores/hashes txids in reverse byte order internally vs. their displayed hex form).
3. Paired and hashed: `Hash(AB) = double_sha256(TxA + TxB)`, `Hash(CD) = double_sha256(TxC + TxD)`.
4. Combined those into the final root: `Merkle Root = double_sha256(Hash(AB) + Hash(CD))`.

**Computed root:** `31630b5976fafe4866f6e7ce545c535e2f5a331f08e4de9d7b118a7c43978cfe`

See `merkle-tree-diagram.png` for the visual tree structure, and `merkle-tree-output.txt` for the full script output showing every intermediate hash.

**Important note:** This computed root does NOT match block 402090's actual merkle root, because the real block contains 192 transactions, not 4. This demonstration uses a manageable 4-transaction subset to clearly show the pairwise-hashing algorithm — the same algorithm Bitcoin applies (recursively, with odd-node duplication) across however many transactions a block actually contains.

## Files

- `README.md` — this file
- `block-inspection.md` — Task 1 results
- `merkle-tree-diagram.png` — visual tree diagram
- `merkle-tree-output.txt` — full script output (all hash levels)
- `code/merkle_tree.py` — Merkle tree construction logic
- `code/generate_diagram.py` — diagram generation script

## Key Learnings

- A block's merkle root allows verifying that a specific transaction is included in a block without needing to download every transaction in that block (this is the basis of SPV/lightweight client proofs).
- Bitcoin's byte-order handling (txids reversed for internal hashing vs. display) is a common source of confusion/bugs when implementing this by hand.
- Odd numbers of transactions at any tree level require duplicating the last hash to keep the pairwise structure valid.
