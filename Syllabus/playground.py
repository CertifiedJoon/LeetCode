def solve_duplicate_subtrees(root):
    ids = dict() # maps triplet to id
    duplicate_roots = []
    
    def generate_id_and_find_duplicate(node):
        if not node:
            return -1
        triplet = (
            generate_id_and_find_duplicate(node.left),
            node.val,
            generate_id_and_find_duplicate(node.right)
        )
        if triplet in ids:
            duplicate_roots.append(node)
        else:
            ids[triplet] = len(ids)
        return ids[triplet]
    
    generate_id_and_find_duplicate(root)
    return duplicate_roots