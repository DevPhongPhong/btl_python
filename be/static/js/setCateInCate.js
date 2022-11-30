$.ajax({
    url: '/api/category',
    type: 'GET',
    success: function (data) {
        const btl_listcate = document.getElementById('btl_listcate')
        btl_listcate.innerHTML = ''
        for (i = 0; i < data.length; i++) {
            btl_listcate.innerHTML += ` <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                            <div class="category-box-layout1">
                                                <figure class="item-figure"><a href="/category/${data[i].id[0]}"><img src="${data[i].main_image[0]}"
                                                            alt="Post"></a></figure>
                                                <div class="item-content">
                                                    <h3 class="item-title"><a href="/category/${data[i].id[0]}">${data[i].name[0]}</a></h3>
                                                </div>
                                            </div>
                                        </div>`
        }
    }
})
