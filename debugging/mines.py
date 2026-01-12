let rows = 10;
let cols = 10;
let mines = 10;

// Ejemplo de estructura: grid[r][c] = { isMine: bool, revealed: bool, ... }
let grid = []; 

let revealedSafeCells = 0;
let gameOver = false;

function revealCell(r, c) {
  if (gameOver) return;

  const cell = grid[r][c];
  if (cell.revealed) return;        // no cuentes dos veces
  if (cell.flagged) return;         // si usas banderas

  cell.revealed = true;

  if (cell.isMine) {
    gameOver = true;
    alert("💥 You hit a mine. Game over!");
    return;
  }

  // Solo cuenta celdas seguras (no-mina)
  revealedSafeCells++;

  // Si tu juego expande ceros, ahí mismo llamarías recursión/cola, PERO
  // asegúrate de que cada celda se marque revealed una sola vez.

  checkWin();
}

function checkWin() {
  const totalSafeCells = rows * cols - mines;
  if (revealedSafeCells === totalSafeCells) {
    gameOver = true;
    alert("✅ You win! All safe cells revealed.");
    // opcional: deshabilitar clicks, mostrar minas, etc.
  }
}

