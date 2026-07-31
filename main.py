from fastapi import FastAPI

app = FastAPI()

student_list = ["Enzo", "JR", "Nyx", "Taz"]


@app.get("/student/{student_id}")
async def get_student(student_id: int):
    return {"message": student_list[student_id]}


@app.post("/student/{student_name}")
async def create_student(student_name: str):
    student_list.append(student_name)
    return {"message": f"Student {student_name} created successfully"}


@app.put("/student/{student_id}")
async def update_student(student_id: int, student_name: str):
    student_list[student_id] = student_name
    return {"message": f"Student {student_id} updated successfully to {student_name}"}


@app.delete("/student/{student_id}")
async def delete_student(student_id: int):
    del student_list[student_id]
    return {"message": f"Student {student_id} deleted successfully"}


@app.get("/student/{student_list}")
async def get_all_student(student_list: list):
    student_list = ["Enzo", "JR", "Nyx", "Taz"]
    return {"message": f"All students: {student_list}"}
