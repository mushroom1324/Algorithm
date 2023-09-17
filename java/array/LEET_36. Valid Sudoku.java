class Solution {
    private char[][] board;
    
    public boolean isValidSudoku(char[][] board) {
        this.board = board;

        for (int i = 0; i < 9; ++i) {
            if (!checkCol(i)) return false;
            if (!checkRow(i)) return false;
        }
        
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (!checkBox(i * 3, j * 3)) return false;
            }
        }
        
        return true;
    }

    private boolean checkCol(int n) {
        int[] arr = new int[9];
        for (int i = 0; i < 9; ++i) {
            if (board[i][n] == '.') continue;
            if (++arr[board[i][n] - '0' - 1] > 1) return false;
        }
        return true;
    }

    private boolean checkRow(int n) {
        int[] arr = new int[9];
        for (int i = 0; i < 9; ++i) {
            if (board[n][i] == '.') continue;
            if (++arr[board[n][i] - '0' - 1] > 1) return false;
        }
        return true;
    }

    private boolean checkBox(int rowStart, int colStart) {
        int[] arr = new int[9];
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                char c = board[rowStart + i][colStart + j];
                if (c == '.') continue;
                if (++arr[c - '0' - 1] > 1) return false;
            }
        }
        return true;
    }
}
