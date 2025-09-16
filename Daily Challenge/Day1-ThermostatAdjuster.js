function adjustThermostat(temp, target) {
    const setTo = null
    
    if (Math.abs(temp < target)) {
        temp = 'heat'
    } else if (Math.abs(temp > target)) {
        temp = 'cool'
    } else 
        return temp = 'hold'
    
    
    return temp
}