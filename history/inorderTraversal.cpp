#include <bits/stdc++.h>
using namespace std;

class RecursiveSolution{
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nums = {};
        helper(root, nums);
        return nums;
    }

private:
    void helper(TreeNode* root, vector<int> &nums){
        if(root == nullptr)
            return;

        helper(root->left, nums);
        nums.push_back(root->val);
        helper(root->right, nums);

        return;
    }
};

class MorrisSolution{
public:
    vector<int> inorderTraversal(TreeNode* root){
        vector<int> nums;
        while(root){
            if (root->left){
                TreeNode* pre = root->left;

                if (pre->right && pre->right != root){
                    pre = pre->right;
                }

                if(!pre->right){
                    pre->right = root;
                    root = root->left;
                } else {
                    pre->right = NULL;
                    nums.push_back(root->val);
                    root = root->right;
                }
            } else {
                nums.push_back(root->val);
                root = root->right;
            }
        }
        return nums;
    }
}
