class Solution_1 {
public:
    vector<vector<int>> levelOrder(TreeNode* root) { // space O(n) -> o(n/2) + o(n/2) + o(n)
        queue<int> depth;
        queue<TreeNode*> q;
        vector<vector<int>> v;

        if (root == NULL)
            return v;
        else {
            q.push(root);
            depth.push(0);
        }

        while (q.size()){
            TreeNode* node = q.front();
            q.pop();
            int d = depth.front();
            depth.pop();

            if (d == v.size())
                v.push_back(vector<int> ());

            v[d].push_back(node->val);

            if (node->left) {
                depth.push(d + 1);
                q.push(node->left);
            }

            if (node->right) {
                depth.push(d + 1);
                q.push(node->right);
            }
        }
        return v;
    }
};

class Solution_2 { //faster O(n) but same storage use as the solution one O(n)
public:
    vector<vector<int> > levelOrder(TreeNode *root) {
        buildVector(root, 0);
        return ret;
    }

private:
    vector<vector<int>> ret;

    void buildVector(TreeNode *root, int depth)
    {
        if(root == NULL) return;
        if(ret.size() == depth)
            ret.push_back(vector<int>());

        ret[depth].push_back(root->val);
        buildVector(root->left, depth + 1);
        buildVector(root->right, depth + 1);
    }
};
