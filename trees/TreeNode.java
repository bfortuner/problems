package trees;

import java.util.List;
import java.util.ArrayList;

public class TreeNode {
    TreeNode parent;
    Integer value;
    List<TreeNode> children = new ArrayList();

    public TreeNode(int value) {
        this.value = value;
    }
    public void setParent(TreeNode node) {
        parent = node;
    }
    public TreeNode getParent() {
	return parent;
    }
    public void setValue(int val) {
	this.value = val;
    }
    public int getValue() {
	return value;
    }
    public TreeNode getChild(int index) {
        return children.get(index);
    }
    public List<TreeNode> getChildren() {
        return children;
    }
    public void setChildren(List<TreeNode> subTree) {
        children = subTree;
    }

}
