var receiveFormApp = new Vue({
    el: '#operationFormApp',
    created: function () {
        let preselectedProductId = $("#hidden_product_id").val()
        if (preselectedProductId) {
            this.product = preselectedProductId
        }
    },
    data: {
        product: '',
        price: '',
        options: []
    },
    watch: {
        product: function (newVal, oldVal) {
            if (newVal) {
                this.update_prices(newVal)
            } else {
                this.options = []
            }
        }
    },
    methods: {
        update_prices: function (product_id) {
            var self = this
            $.ajax({
                url: '/catalogue/price/get/'+$("#form_model").val()+'/' + product_id,
                method: 'GET',
                success: function (data) {
                    self.options = data
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    }


});