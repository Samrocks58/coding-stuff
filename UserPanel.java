import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class UserPanel extends JPanel implements JavaArcade, KeyListener, ActionListener {

    private boolean isRunning;
    private int score;
    private Timer timer;
    private boolean timerRunning;
    private String highScore = "0";
    private int width = 600;
    private int height = 450;
    private int playerWidth = 30;
    private int playerHeight = playerWidth;
    private int MoveX;
    private int MoveY;


    public UserPanel(int w, int h) {
        this.addKeyListener(this);
        width = w;
        height = h;
        MoveX = width/2-playerWidth/2;
        MoveY = height/2-playerHeight/2;
//        timer = new javax.swing.Timer(50, this);
    }

    public boolean running() {
        return isRunning;
    }

    public void startGame() {
        isRunning = true;
        timerRunning = true;
        score = 0;
    }

    public String getGameName() {
        return "Cool Game Name";
    }

    public void pauseGame() {
        timerRunning = false;
    }

    public void stopGame() {
        isRunning = false;
        score = 0;
    }

    public String getInstructions() {
        return "1. DO thing\n2. DO gOOd\n3. DO BETTER";
    }

    public String getCredits() {
        return "Samuel Pearce";
    }

    public String getHighScore() {
        return highScore;
    }

    public int getPoints() {
        return score;
    }

    public void setDisplay(GameStats d) {
        d.update(score);
        if (!(isRunning)) {
            d.gameOver(score);
        }

    }

    public void keyTyped(KeyEvent e) {}

    public void keyPressed(KeyEvent e) {
        char input = e.getKeyChar();
//        System.out.println(input);
        if (input == 'q') {
            System.exit(-1);
        }else if (input == 'w') {
            MoveY -= playerHeight;
        }else if (input == 'a') {
            MoveX -= playerWidth;
        }else if (input == 's') {
            MoveY += playerHeight;
        }else if (input == 'd') {
            MoveX += playerWidth;
        }
        repaint();
    }

    public void keyReleased(KeyEvent e) {}

    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        g.setColor(Color.RED);
        g.fillRect(MoveX, MoveY, 30, 30);
    }

    public void actionPerformed(ActionEvent e) {
        repaint();
    }
}
