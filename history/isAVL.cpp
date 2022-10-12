class Solution {
public:
   bool isBalanced(TreeNode* root) {
       if (root == NULL)
           return true;

       return abs(height(root->left) - height(root->right)) <= 1
               && isBalanced(root->right) && isBalanced(root->left);
   }

private:
   int height(TreeNode* root){
       if (root == NULL)
           return -1;

       return 1 + max(height(root->left), height(root->right));
   }

};
