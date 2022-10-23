package classes;

import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class FiltroFaturas {
    private ArrayList<String> estadosDoSul;

    public FiltroFaturas() {
        this.estadosDoSul = new ArrayList<String>();
        this.estadosDoSul.add("SC");
        this.estadosDoSul.add("RS");
        this.estadosDoSul.add("PR");
    }

    public Boolean atendeCondicao1(Fatura fatura) {
        return fatura.getValor() < 2000;
    }

    public Boolean atendeCondicao2(Fatura fatura) {
        Period age = Period.between(fatura.getData(), LocalDate.now());

        return (fatura.getValor() >= 2000 && fatura.getValor() <= 2500) && age.getMonths() >= 1;
    }

    public Boolean atendeCondicao3(Fatura fatura) {
        Period age = Period.between(fatura.getCliente().getDataInclusao(), LocalDate.now());

        return (fatura.getValor() >= 2500 && fatura.getValor() <= 3000) && age.getMonths() >= 2;
    }

    public Boolean atendeCondicao4(Fatura fatura) {
        String estadoCliente = fatura.getCliente().getEstado();

        return fatura.getValor() >= 4000 && this.estadosDoSul.contains(estadoCliente);
    }

    public ArrayList<Fatura> filtrarFaturas(ArrayList<Fatura> faturas) {
        for (int i = 0; i < faturas.size(); i++) {
            Boolean removeFatura = atendeCondicao1(faturas.get(i)) || atendeCondicao2(faturas.get(i)) || atendeCondicao3(faturas.get(i)) || atendeCondicao4(faturas.get(i));

            if (removeFatura) {
                faturas.remove(i);
            }
        }

        return faturas;
    }
}
