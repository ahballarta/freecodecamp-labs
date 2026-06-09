# Game Character Stats Tracker

## Español

Este laboratorio implementa un sistema de seguimiento de estadísticas para personajes de videojuegos utilizando Python. El proyecto fue desarrollado para practicar programación orientada a objetos, encapsulamiento, propiedades y validación de atributos.

### Requisitos

El proyecto define una clase GameCharacter con las siguientes funcionalidades:

- Almacena el nombre, la salud, el maná y el nivel del personaje.
- Proporciona acceso de solo lectura al nombre del personaje.
- Utiliza propiedades para gestionar los atributos de salud y maná.
- Impide que la salud sea menor que 0 o mayor que 100.
- Impide que el maná sea menor que 0 o mayor que 50.
- Permite consultar el nivel actual del personaje.
- Incluye un método level_up() que:
  - Incrementa el nivel en una unidad.
  - Restaura la salud a 100.
  - Restaura el maná a 50.
  - Muestra un mensaje indicando el nuevo nivel alcanzado.
- Implementa un método __str__() para mostrar las estadísticas actuales del personaje.

### Conceptos Practicados

- Programación Orientada a Objetos (OOP)
- Encapsulamiento
- Propiedades (@property)
- Getters y setters
- Validación de datos
- Gestión de estados
- Métodos especiales (__str__)
- Diseño de clases

### Ejemplo de Salida

```text
Name: Kratos
Level: 1
Health: 100
Mana: 50

Kratos leveled up to 2!
Name: Kratos
Level: 2
Health: 100
Mana: 50
```

### Estado

✅ Completado

---

## English

This lab implements a game character stats tracker in Python. The project was developed to practice object-oriented programming, encapsulation, properties, and attribute validation.

### Requirements

The project defines a GameCharacter class with the following functionality:

- Stores the character's name, health, mana, and level.
- Provides read-only access to the character name.
- Uses properties to manage health and mana values.
- Prevents health from dropping below 0 or exceeding 100.
- Prevents mana from dropping below 0 or exceeding 50.
- Allows access to the character's current level.
- Includes a level_up() method that:
  - Increases the level by one.
  - Restores health to 100.
  - Restores mana to 50.
  - Displays a level-up message.
- Implements a custom __str__() method to display the character's current statistics.

### Concepts Practiced

- Object-Oriented Programming (OOP)
- Encapsulation
- Properties (@property)
- Getters and setters
- Data validation
- State management
- Special methods (__str__)
- Class design

### Example Output

```text
Name: Kratos
Level: 1
Health: 100
Mana: 50

Kratos leveled up to 2!
Name: Kratos
Level: 2
Health: 100
Mana: 50
```

### Status

✅ Completed

---

Completed as part of the freeCodeCamp Python Certification.
