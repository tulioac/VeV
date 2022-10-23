package classes;

import java.time.LocalDate;

public class Cliente {
    private String nome;
    private String estado;
    private LocalDate dataInclusao;

    public Cliente(String nome, String estado, LocalDate dataInclusao) {
        this.nome = nome;
        this.estado = estado;
        this.dataInclusao = dataInclusao;
    }

    public String getEstado() {
        return this.estado;
    }

    public LocalDate getDataInclusao() {
        return this.dataInclusao;
    }
}
