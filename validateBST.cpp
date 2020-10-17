class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return nodecheck(root, LONG_MIN, LONG_MAX);
    }

    bool nodecheck(TreeNode* root, long min, long max){
        if (root == NULL)
            return true;

        return root->val < max && root->val > min
                && nodecheck(root->left, min, root->val)
                && nodecheck(root->right, root->val, max);
    }
};
