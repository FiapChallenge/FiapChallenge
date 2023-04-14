import br.com.fiap.model.RoyalBard;
import br.com.fiap.model.Song;
import br.com.fiap.model.Author;

public class App {
    public static void main(String[] args) throws Exception {
        RoyalBard rb = new RoyalBard();
        rb.addAuthor("Taka");

        Author enygma = new Author("Enygma");
        rb.addAuthor(enygma);
        rb.addAuthor("kant");

        rb.addSong("Taka", "Ultimo Trago", "https://www.youtube.com/watch?v=hGQvHnNDQkk");
        rb.addSong("Taka", "Lua de Neon", "https://www.youtube.com/watch?v=f9U4v17rHr0");

        Song lampadasNegras = new Song(enygma, "Lampadas Negras", "https://www.youtube.com/watch?v=OkguEVkpR3I");
        rb.addSong(lampadasNegras);
        
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
