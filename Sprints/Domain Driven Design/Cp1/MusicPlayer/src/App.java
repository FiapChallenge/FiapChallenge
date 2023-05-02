import br.com.fiap.model.RoyalBard;
import br.com.fiap.model.Song;
import br.com.fiap.model.Author;
import br.com.fiap.model.Usuario;
import br.com.fiap.model.Album;

public class App {
    public static void main(String[] args) throws Exception {
        RoyalBard rb = new RoyalBard();
        Author taka = new Author("Taka");
        Author enygma = new Author("Enygma");
        Author kant = new Author("kant");
        Author setemin = new Author("7 Minutoz");
        rb.addAuthor(enygma);
        rb.addAuthor(taka);
        rb.addAuthor(kant);
        rb.addAuthor(setemin);

        Song songUltimoTrago = new Song(taka, "Ultimo Trago", "https://www.youtube.com/watch?v=hGQvHnNDQkk");
        Song songLuaDeNeon = new Song(taka, "Lua de Neon", "https://www.youtube.com/watch?v=f9U4v17rHr0");
        Song lampadasNegras = new Song(enygma, "Lampadas Negras", "https://www.youtube.com/watch?v=OkguEVkpR3I");
        rb.addSong(songUltimoTrago);
        rb.addSong(songLuaDeNeon);
        rb.addSong(lampadasNegras);

        Song songAlma = new Song(enygma, "Alma", "https://www.youtube.com/watch?v=TvmVibumIOs");
        Song songMorte = new Song(enygma, "Morte", "https://www.youtube.com/watch?v=RyJrVTEFoDQ");
        Song songPurgatorio = new Song(kant, "Purgatório", "Rap", 2022, 178,
                "https://www.youtube.com/watch?v=BGSUkniD_Rw");
        rb.addSong(songAlma);
        rb.addSong(songMorte);
        rb.addSong(songPurgatorio);

        Song songValeDoFim = new Song(setemin, "Vale do Fim", "https://www.youtube.com/watch?v=v7lgtAaJsFg");
        Song songShippuden = new Song(setemin, "Shippuden", "https://www.youtube.com/watch?v=eiANVt-Kr_s");
        Song songRinnegan = new Song(setemin, "Rinnegan", "https://www.youtube.com/watch?v=8LLNdqZmRho");
        Song songKaton = new Song(setemin, "Katon", "https://www.youtube.com/watch?v=FTrqVV7xOPo");
        rb.addSong(songValeDoFim);
        rb.addSong(songShippuden);
        rb.addSong(songRinnegan);
        rb.addSong(songKaton);

        Album albumJinchuriki = new Album("Jinchuriki", setemin, 2021);
        setemin.addAlbum(albumJinchuriki);
        albumJinchuriki.addSong(songValeDoFim);
        albumJinchuriki.addSong(songShippuden);
        albumJinchuriki.addSong(songRinnegan);
        albumJinchuriki.addSong(songKaton);

        Usuario asteriuz = new Usuario("Asteriuz", "pandorinha");
        asteriuz.addFavoriteSong(songUltimoTrago);
        asteriuz.addFavoriteSong(songLuaDeNeon);
        asteriuz.addFavoriteSong(lampadasNegras);
        asteriuz.addFavoriteSong(songPurgatorio);

        setemin.showAlbuns();
        albumJinchuriki.showSongs();
        asteriuz.showFavoriteSongs();
        rb.getAuthor("kant").setName("Kant");
        // rb.getAuthor("Taka").showSongs();
        // rb.getAuthor("Enygma").showSongs();
        rb.showSongs();
        // rb.showAuthors();
        rb.play("Lua de Neon");
        // rb.play("Alma", "Enygma");
        // rb.playRandom();
    }
}
