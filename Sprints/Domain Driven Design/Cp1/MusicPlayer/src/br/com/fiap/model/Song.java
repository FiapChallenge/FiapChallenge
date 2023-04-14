package br.com.fiap.model;

public class Song {
    private Author author;
    private String title;
    private String genre;
    private int year;
    private int duration;
    private String youtubePath;

    public Song(Author author, String title, String youtubePath) {
        this.author = author;
        this.title = title;
        this.youtubePath = youtubePath;
        this.author.addSong(this);
    }

    public Song(Author author, String title, String genre, int year, int duration, String youtubePath) {
        this.author = author;
        this.title = title;
        this.genre = genre;
        this.year = year;
        this.duration = duration;
        this.youtubePath = youtubePath;
        this.author.addSong(this);
    }

    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public String getYoutubePath() {
        return youtubePath;
    }

    public void setYoutubePath(String youtubePath) {
        this.youtubePath = youtubePath;
    }

    @Override
    public String toString() {
        return "Song [author=" + author + ", title=" + title + "]";
    }

}
