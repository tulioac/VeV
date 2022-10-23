package classes;

import java.time.LocalDate;

public class Fatura {
    private Integer codigo;
    private Double valor;
    private LocalDate data;
    private Cliente cliente;

    public Fatura(Integer codigo, Double valor, LocalDate data, Cliente cliente) {
        this.codigo = codigo;
        this.valor = valor;
        this.data = data;
        this.cliente = cliente;
    }

    public Double getValor() {
        return this.valor;
    }

    public Cliente getCliente() {
        return this.cliente;
    }

    public LocalDate getData() {
        return this.data;
    }
}
