package classes;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.text.ParseException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class FiltroFaturasTest {

    @Test
    @DisplayName("Checa se o valor da fatura é menor que 2000 reais")
    void checaSeAtendeCondicao1() {
        Cliente cliente = new Cliente("carol", "PB", LocalDate.now());
        Fatura fatura = new Fatura(1, 1999.9, LocalDate.now(), cliente);

        FiltroFaturas filtro = new FiltroFaturas();

        assertEquals(true, filtro.atendeCondicao1(fatura));
    }

    @Test
    @DisplayName("Checa se o valor da fatura esta entre 2000 e 2500 reais e se na fatura consta uma data referente a 1 mês atras ou mais")
    void checaSeAtendeCondicao2() throws ParseException {
        Cliente cliente = new Cliente("carol", "PB", LocalDate.now());

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String date = "16/09/2022";

        //convert String to LocalDate
        LocalDate localDate = LocalDate.parse(date, formatter);

        Fatura fatura = new Fatura(1, 2025.0, localDate, cliente);

        FiltroFaturas filtro = new FiltroFaturas();

        assertEquals(true, filtro.atendeCondicao2(fatura));
    }

    @Test
    @DisplayName("Checa se o valor da fatura esta entre 2500 e 3000 reais e se a data de inclusao do cliente é de 1 mes atras ou mais")
    void checaSeAtendeCondicao3() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String date = "16/06/2022";

        //convert String to LocalDate
        LocalDate localDate = LocalDate.parse(date, formatter);
        Cliente cliente = new Cliente("carol", "PB", localDate);
        Fatura fatura = new Fatura(1, 2025.0, LocalDate.now(), cliente);

        FiltroFaturas filtro = new FiltroFaturas();

        assertEquals(true, filtro.atendeCondicao3(fatura));
    }

    @Test
    @DisplayName("Checa se o valor da fatura é maior que 4000 reais e se o cliente pertence a algum estado do sul")
    void checaSeAtendeCondicao4() {
        Cliente cliente = new Cliente("carol", "SC", LocalDate.now());
        Fatura fatura = new Fatura(1, 4098.0, LocalDate.now(), cliente);

        FiltroFaturas filtro = new FiltroFaturas();

        assertEquals(true, filtro.atendeCondicao4(fatura));
    }

    @Test
    @DisplayName("Remove a fatura da lista se ela atender alguma das condicoes testadas acima")
    void filtraFaturas() {
        Cliente cliente1 = new Cliente("carol", "PB", LocalDate.now());
        Fatura fatura1 = new Fatura(1, 1999.9, LocalDate.now(), cliente1);

        Cliente cliente2 = new Cliente("julia", "PB", LocalDate.now());

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String date = "16/10/2022";
        LocalDate localDate = LocalDate.parse(date, formatter);
        Fatura fatura2 = new Fatura(1, 2025.0, localDate, cliente2);

        Cliente cliente3 = new Cliente("fabio", "SC", LocalDate.now());
        Fatura fatura3 = new Fatura(1, 4098.0, LocalDate.now(), cliente3);

        ArrayList<Fatura> faturas = new ArrayList<Fatura>();
        faturas.add(fatura1);
        faturas.add(fatura2);
        faturas.add(fatura3);

        FiltroFaturas filtro = new FiltroFaturas();
        ArrayList<Fatura> teste = new ArrayList<Fatura>();
        teste.add(fatura2);

        assertArrayEquals(teste.toArray(), filtro.filtrarFaturas(faturas).toArray());
    }

}