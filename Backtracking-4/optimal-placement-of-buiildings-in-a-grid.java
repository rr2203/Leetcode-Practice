// TC: O((HW)^(N+1)) | SC: O(HW)
public class Main {
    public static void main(String[] args) {

        BuildingPlacement buildingPlacement = new BuildingPlacement();

        System.out.print(buildingPlacement.findMinDistance(5, 5, 4));

    }

    public static class BuildingPlacement{

        int minDist = Integer.MAX_VALUE;

        int H; int W;

        int [][] result;

        public int findMinDistance(int h, int w, int n){

            this.H = h; this.W = w;

            int [][] grid = new int[h][w];

            for(int i = 0; i < H; i++){

                for(int j = 0; j < W; j++){

                    grid[i][j] = -1;

                }

            }

            backtrack(grid, n, 0);

            // System.out.print(Arrays.deepToString(result));

            return minDist;

        }

        private void bfs(int [][] grid){

            Queue<int []> q = new LinkedList<>();

            boolean [][] visited = new boolean[H][W];

            int [][] dirs = {{0,1}, {0,-1}, {1, 0}, {-1, 0}};

            for(int i = 0; i< H; i++){

                for(int j = 0; j < W; j++){

                    if(grid[i][j] == 0){

                        q.add(new int[]{i, j});

                        visited[i][j] = true;

                    }

                }

            }

            //process bfs

            int dist = 0;

            while(!q.isEmpty()){

                int size = q.size();

                for(int i = 0; i < size; i++){

                    int [] curr = q.poll();

                    for(int [] dir: dirs){

                        int nr = curr[0] + dir[0];

                        int nc = curr[1] + dir[1];

                        if(nr >= 0 && nc >= 0 && nr < H

                           && nc < W && !visited[nr][nc]){

                            q.add(new int[]{nr, nc});

                            visited[nr][nc] = true;

                        }

                    }

                }

                dist++;

            }

            if(minDist > dist -1){

                result = grid;

                if(dist - 1 == 2){

                    System.out.print(Arrays.deepToString(result));

                }

                 

            }

            minDist = Math.min(minDist, dist-1);

        }

        private void backtrack(int [][] grid, int n, int idx){

            //base

            if(n == 0){

                bfs(grid);

            }

            // logic

            for(int j = idx; j < H*W; j++){

                int r = j/W;

                int c = j%W;

                grid[r][c] = 0;

                //recurse

                backtrack(grid, n - 1, j+1);

                // backtrack

                grid[r][c] = -1;

            }
        }
    }
}