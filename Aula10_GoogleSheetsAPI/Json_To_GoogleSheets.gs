// programa em JavaScript feito para receber um JSON e produzir uma Planilha no sheets

function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([new Date(), data.placa, data.carro, data.funcionario]); // nessa linha seta a primeira coluna como data e hora do computador, e depois as colunas adicionadas a planilha. As colunas devem ter o mesmo nome do Arquivo JSON
  return ContentService.createTextOutput("Success");
}

function doGet(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var rows = sheet.getDataRange().getValues();
  var headers = rows.shift();
  var json = rows.map(row => {
    var obj = {};
    headers.forEach((h, i) => obj[h] = row[i]);
    return obj;
  });
  return ContentService.createTextOutput(JSON.stringify(json)).setMimeType(ContentService.MimeType.JSON);
} //aqui da input em todas as colunas os dados na planilha