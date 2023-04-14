package br.com.fiap.view;

import br.com.fiap.model.*;

public class Terminal {
    public static void main(String[] args) {
        RoyalBard rb = new RoyalBard();
        rb.addAuthor("Taka");
        rb.addAuthor("Enygma");
        rb.addAuthor("kant");

        rb.addSong("Taka", "Ultimo Trago", "https://www.youtube.com/watch?v=hGQvHnNDQkk");
        rb.addSong("Taka", "Lua de Neon", "https://www.youtube.com/watch?v=f9U4v17rHr0");
        rb.addSong("Taka", "Lampadas Negras", "https://www.youtube.com/watch?v=OkguEVkpR3I");
        rb.addSong("Enygma", "Alma", "https://www.youtube.com/watch?v=TvmVibumIOs");
        rb.addSong("Enygma", "Morte", "https://www.youtube.com/watch?v=RyJrVTEFoDQ");
        rb.addSong("kant", "Purgatório", "Rap", 2022, 178, "https://www.youtube.com/watch?v=BGSUkniD_Rw");

        rb.getAuthor("kant").setName("Kant");
        // rb.getAuthor("Taka").showSongs();
        // rb.getAuthor("Enygma").showSongs();
        // rb.showSongs();
        // rb.showAuthors();
        // rb.play("Lua de Neon");
        // rb.play("Alma", "Enygma");
        rb.playRandom();
    }
}
