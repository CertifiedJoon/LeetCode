class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL)
            return false;

        if (root->right == NULL && root->left == NULL && root->val == sum)
            return true;

        return hasPathSum(root->right, sum - root->val)
            || hasPathSum(root->left, sum - root->val);
    }
};
