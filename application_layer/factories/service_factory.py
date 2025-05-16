from application_layer.services.employee_service import EmployeeService
from application_layer.services.education_service import EducationService
from application_layer.services.experience_service import ExperienceService
from application_layer.interfaces.database_manager_interface import IDatabaseManager

class ServiceFactory:
    @staticmethod
    def create_employee_service(db_manager: IDatabaseManager) -> EmployeeService:
        return EmployeeService(db_manager)
    
    @staticmethod
    def create_education_service(db_manager: IDatabaseManager) -> EducationService:
        return EducationService(db_manager)
    
    @staticmethod
    def create_experience_service(db_manager: IDatabaseManager) -> ExperienceService:
        return ExperienceService(db_manager)