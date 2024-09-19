//Creacion de un metodo

//Creación de un objeto literal
const user = {
    //Atributos
    name: 'Denilson',
    lastname: 'Morales',
    age: 25,
    city: 'Lima',
    showFullName: function (){
        return `${this.name} ${this.lastname}`
    }

}

const club = {
    name: 'Barcelona',
    lastname: 'Masia',
    age:100,
    city:'Cataluña',
    
}

console.log(user.showFullName())
console.log(club)

