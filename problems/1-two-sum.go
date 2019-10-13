import "fmt"

func twoSum(nums []int, target int) []int {
    
    var nums_map = make(map[int]int)
    
    for i, v := range nums {
        nums_map[v] = i
    }
    
    for i, v := range nums {
        var diff = target - v
        // fmt.Println(diff)
        // fmt.Println(i)
        if v, ok := nums_map[diff]; ok {
            // fmt.Println(v)
            if i == v {
                continue
            }
            return []int{i, v}
        }
    }
    return []int{0}
}