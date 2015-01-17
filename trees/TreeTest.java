package trees;

import java.util.List;
import java.util.ArrayList;

public class TreeTest {

    public static void main(String[] str) {
        Tree tree = new Tree();
        TreeNode n1 = new TreeNode(3);
        tree.setRoot(n1);
        TreeNode n2 = new TreeNode(4);
        TreeNode n3 = new TreeNode(5);
        tree.addChild(n1, n2);
        tree.addChild(n1, n3);

        System.out.println(n2.getParent() == n1);

        System.out.println(n1.getValue() == 3);
        System.out.println(n2.getParent() == n1);

        System.out.println(n1.getChildren().size() == 2);
        System.out.println(n1.getChild(0).getValue() == 4);

        tree.removeChild(n1, 0);

        System.out.println(n1.getChildren().size() == 1);
        System.out.println(n1.getChild(0).getValue() == 5);

        tree.addChild(n1, n2, 0);

        System.out.println(n1.getChildren().size() == 1);
        System.out.println(n1.getChild(0).getValue() == 4);
        System.out.println(n2.getParent() == n1);

        System.out.println(n2.getChildren().size() == 1);
        System.out.println(n2.getChild(0).getValue() == 5);

    }

}
