#Pineda, Lyra BSCS 3A
from typing import Optional
from fastapi import FastAPI, Query, Path

app = FastAPI()
#problem 1
prices_db : list[float] = [15.50 , 99.99 , 45.00 , 250.00 , 12.00 , 500.25 , 75.10]

@app.get("/prices")
async def get_prices(min_price: Optional[float] = Query(ge=0.0), max_price: Optional[float] = Query(le=1000.0)):
    filtered_prices = [price for price in prices_db if (min_price is None or price >= min_price) and (max_price is None or price <= max_price)]  

    return {"filtered_prices":filtered_prices, "count": len(filtered_prices)}

#problem 2
employee_db : dict[int , str] = {
1001: "Diego Tian",
1002: "Paul Lee",
1003: "Diego Paul Lee Tian"
}

@app.get("/employees/{emp_id}")
async def get_employee(emp_id: int = Path(title = "Employee ID", description = "4-digit internal employee  code",  ge=1, lt=1000)):
   if emp_id in employee_db:
     return {
        
     }
   else: return {"error": "Employee not found"}



#problem 3
from typing import Dict
from fastapi import FastAPI, Path, Query

app = FastAPI()

tasks_db: list[str] = [" Setup environment ", "Write unit tests", "Deploy application\n"]

@app.get("/tasks")
async def get_tasks() -> Dict[str, object]:
    return {"tasks": tasks_db, "total_count": len(tasks_db)}

@app.post("/tasks")
async def create_task(
    task_name: str = Query(..., min_length=3, max_length=50)
) -> Dict[str, object]:
    tasks_db.append(task_name)
    return {"tasks": tasks_db, "total_count": len(tasks_db)}

@app.delete("/tasks/{task_index}")
async def delete_task(
    task_index: int = Path(..., ge=0)
) -> Dict[str, object]:
    if 0 <= task_index < len(tasks_db):
        deleted_task = tasks_db.pop(task_index)
        return {"message": "Task removed", "deleted": deleted_task}
    return {"error": "Index out of range"}

#problem 4
inventory_db: dict[int, str] = {
  501: " Mechanical Keyboard",
  502: " Ergonomic Mouse",
  503: "USB -C Hub",
}

@app.get("/inventory")
async def get_inventory() -> Dict[int, str]:
  return inventory_db


@app.get("/inventory/{item_id}")
async def get_inventory_item(
  item_id: int = Path(..., gt=0)
) -> Dict[str, object]:
  if item_id in inventory_db:
      return {"item_id": item_id, "item_name": inventory_db[item_id]}
  return {"error": "Item not found"}


@app.post("/inventory/{item_id}")
async def create_inventory_item(
  item_id: int = Path(..., gt=0),
  item_name: str = Query(..., min_length=2, max_length=30),
) -> Dict[str, object]:
  inventory_db[item_id] = item_name
  return {"message": "Item added", "item_id": item_id, "item_name": item_name}


@app.delete("/inventory/{item_id}")
async def delete_inventory_item(
  item_id: int = Path(..., gt=0)
) -> Dict[str, object]:
  if item_id in inventory_db:
      del inventory_db[item_id]
      return {"message": "Item removed", "item_id": item_id}
  return {"error": "Item not found"}



