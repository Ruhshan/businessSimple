var receiveFormApp = new Vue({
    el: '#receiveFormApp',
    data:{
        product:'',
        price:'',
        prices : []
    },
    watch:{
        product: function (newVal, oldVal) {
            if(newVal){
                this.update_prices(newVal)
            }else{
                this.prices=[]
            }
        }
    },
    methods:{
        update_prices:function (product_id) {
            var self = this
            $.ajax({
            url: '/catalogue/price/get/'+product_id,
            method: 'GET',
            success: function (data) {
                self.prices = data
            },
            error: function (error) {
                console.log(error);
            }
        });
        }
    }


});