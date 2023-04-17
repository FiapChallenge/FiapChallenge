package br.com.fiap.model;

import java.util.ArrayList;
import java.util.List;

public class Album {
    private String name;
    private Author author;
    private int year;
    private List<Song> songs = new ArrayList<>();

    public Album(String name, Author author, int year) {
        this.name = name;
        this.author = author;
        this.year = year;
    }

    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void addSong(Song song) {
        this.songs.add(song);
    }

    public void showSongs() {
        System.out.print("Songs of " + this.name + ": ");
        boolean last = false;
        for (Song song : this.songs) {
            last = this.songs.indexOf(song) == this.songs.size() - 1;
            if (last) {
                System.out.println(song.getTitle());
            } else {
                System.out.print(song.getTitle());
                System.out.print(", ");
            }
        }
    }

}
