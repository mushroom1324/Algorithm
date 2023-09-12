class Solution {
    public void solve(char[][] board) {
        for (int i = 0; i < board.length; ++i) {
            if (board[i][0] != 'X') DFS(i, 0, board);
            if (board[i][board[0].length - 1] != 'X') DFS(i, board[0].length - 1, board);
        }

        for (int i = 0; i < board[0].length - 1; ++i) {
            if (board[0][i] != 'X') DFS(0, i, board);
            if (board[board.length - 1][i] != 'X') DFS(board.length - 1, i, board);
        }

        swap(board, 'O', 'X');
        swap(board, 'p', 'O');
    }

        void swap(char[][] board,char p, char q){
        for(int i=0;i<board.length;i++)
            for(int j=0;j<board[0].length;j++)
                    if(board[i][j]==p) board[i][j]=q;
    }

    void DFS(int i,int j, char[][] board){
        if(!(i>=0 && j>=0 && i<board.length && j<board[0].length && board[i][j]=='O')) return ;
        board[i][j]='p';
        DFS(i+1,j,board);
        DFS(i,j+1,board);
        DFS(i-1,j,board);
        DFS(i,j-1,board);
    }
}
