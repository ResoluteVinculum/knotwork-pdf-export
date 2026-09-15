# Summary
1. Override basically everything, make the modal display the raw md and the PDF preview using the currently used theme.
2. Make the pre-render processing look for page break ("///") symbols and replace with '<div class="page-break" style="break-after:page;"></div>'.
3. Keep the pagination and working links, somehow...