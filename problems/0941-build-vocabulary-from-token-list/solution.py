def build_vocab(tokens):
    """
    Build a vocabulary dictionary from a list of tokens.

    Args:
        tokens: list of string tokens

    Returns:
        Dict mapping each unique token (sorted) to a unique integer ID starting from 0.
    """
    # 第一步：使用 set 去除重复的 token
    unique_tokens = set(tokens)

    # 第二步：将 token 按字典顺序排序
    sorted_tokens = sorted(unique_tokens)

    # 第三步：创建一个空字典，用来保存 token 和 ID 的对应关系
    vocab = {}

    # 第四步：依次给每个 token 分配 ID
    for i in range(len(sorted_tokens)):
        token = sorted_tokens[i]
        vocab[token] = i

    # 第五步：返回最终的字典
    return vocab

    pass
