package trees;

import java.util.List;
import java.util.ArrayList;

public class Tree {
    TreeNode root;

    public void setRoot(TreeNode node) {
        root = node;
    }
    public TreeNode getRoot() {
        return root;
    }
    public void addChild(TreeNode parent, TreeNode newChild) {
        newChild.setParent(parent);
        parent.getChildren().add(newChild);
    }
    public void addChild(TreeNode parent, TreeNode newChild, int index) {
        newChild.setParent(parent);
        List<TreeNode> children = parent.getChildren();
        TreeNode curChild = children.get(index);
        curChild.setParent(newChild);
        newChild.getChildren().add(curChild);
        children.set(index, newChild);
    }
    /*
     * Removes element at index 3, returns element,
     * shifts remaining elements to the left, resizing the list
     */
    public void removeChild(TreeNode parent, int index) {
        parent.getChildren().remove(index);
    }

}
