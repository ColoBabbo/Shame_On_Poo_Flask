
let autocomplete
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('location'), {
        types: ['street_address'],
        componentRestrictions: { 'country': ['US'] },
        fields: ['name']
    }
    )
}
