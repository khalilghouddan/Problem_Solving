# ============================================================
# Fixed-Size Text Chunking with Overlap
# ============================================================
#
# Splitting long documents into smaller, overlapping chunks is
# a fundamental step in building Retrieval-Augmented Generation
# (RAG) applications.
#
# Task:
# Implement the function:
#
#     fixed_size_chunking(text, chunk_size, overlap_size)
#
# Requirements:
#
# 1. Split the input string `text` into chunks of
#    `chunk_size` characters.
#
# 2. Move the sliding window forward by:
#
#        step = chunk_size - overlap_size
#
# 3. Raise a ValueError if `overlap_size` is greater than or
#    equal to `chunk_size`.
#
# 4. Raise a ValueError if `chunk_size` is less than or equal
#    to 0.
#
# 5. If `text` is empty, return an empty list [].
#
# Example:
#
#     fixed_size_chunking("abcdefgh", 4, 2)
#
#     # Returns:
#     ["abcd", "cdef", "efgh"]
#
# Explanation:
#
#     chunk_size = 4
#     overlap_size = 2
#     step = 4 - 2 = 2
#
#     "abcdefgh"
#     ├── "abcd"
#     │     └── overlap: "cd"
#     ├────── "cdef"
#     │        └── overlap: "ef"
#     └──────── "efgh"
#
# Key concept:
# The overlap preserves contextual information between
# consecutive chunks, which can improve retrieval quality
# in RAG systems.
#
# ============================================================



from typing import List

def fixed_size_chunking(
    text: str, 
    chunk_size: int, 
    overlap_size: int
) -> List[str]:
    # Your code here
  
    if chunk_size <= 0:
      raise ValueError("chunkSize must be greater than 0")

    if overlap_size >= chunk_size:
      raise ValueError("ovela^pSize must be less than chunkSize")

    if not text:
      return []

    chunks = []

    #we must calcule the steeeep
    step=chunk_size-overlap_size
    
    for i in range(0, len(text), step):
  
      chunk = text[i:i + chunk_size]

      chunks.append(chunk)

      if i+chunk_size >= len(text):
        break
      
    return chunks 





