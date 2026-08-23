# features/projects/services.py
def create_project_logic(name: str, client_name: str, total_budget: float):
    if not name or total_budget <= 0:
        return {"status": "failed", "message": "Nama proyek dan anggaran harus valid"}
    
    return {
        "status": "success",
        "project_id": 101,
        "name": name,
        "client_name": client_name,
        "total_budget": total_budget,
        "project_status": "ON_PROGRESS"
    }