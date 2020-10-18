class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return isSymmetric(root, root);
    }
private:
    bool isSymmetric(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL)
            return true;
        if (!q || ! p || p->val != q->val)
            return false;
        return isSymmetric(p->left,q->right) && isSymmetric(p->right, q->left);
    }
};
