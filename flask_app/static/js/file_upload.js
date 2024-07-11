const show_url = () => {
    radio_choice.innerHTML = `
        <input 
            class="form-control" 
            type="url" 
            name="img_file" 
            id="img_file_or_url" 
            placeholder="URL:">
    `
}

const show_file = () => {
    radio_choice.innerHTML = `
        <input 
            class="form-control" 
            type="file" 
            accept="image/*" 
            name="img_file" 
            id="img_file_or_url">
    `
}