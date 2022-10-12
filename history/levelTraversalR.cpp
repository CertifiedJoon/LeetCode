#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        int height = get_height(root);

        while(height){
            v.push_back(vector<int>());
            height--;
        }

        buildVector(root, 0);
        return v;
    }

private:
    vector<vector<int>> v;

    void buildVector(TreeNode* root, int depth){
        if (root == nullptr)
            return;

        v.rbegin()[depth].push_back(root->val);

        buildVector(root->left, depth + 1);
        buildVector(root->right, depth + 1);
    }

    int get_height (TreeNode* root){
        if (root == nullptr)
            return 0;

        return 1 + max(get_height(root->left), get_height(root->right));
    }
};
