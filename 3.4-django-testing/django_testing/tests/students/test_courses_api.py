import pytest


@pytest.mark.django_db
def test_get_course(client, courses_factory):
    courses = courses_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 200

    data = response.json()
    assert courses[0].name == data['name']


@pytest.mark.django_db
def test_get_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_courses_by_id(client, courses_factory):
    courses = courses_factory(_quantity=1000)
    response = client.get(f'/api/v1/courses/?id={courses[100].id}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[100].id


@pytest.mark.django_db
def test_filter_courses_by_name(client, courses_factory):
    courses_factory(_quantity=10)
    courses_factory(name='TARGET')

    response = client.get('/api/v1/courses/?name=TARGET')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == 'TARGET'


@pytest.mark.django_db
def test_create_course(client, student_factory):
    students = student_factory(_quantity=10)

    data = {
        'name': 'TEST',
        'students': [student.id for student in students]
    }
    response = client.post('/api/v1/courses/', data=data, format='json')
    assert response.status_code == 201

    response = response.json()

    assert response['name'] == "TEST"


@pytest.mark.django_db
def test_update_course(client, student_factory, courses_factory):
    courses = courses_factory(_quantity=10, id=1)
    students = student_factory(_quantity=10)

    data = {
        'name': 'UPDATED NAME',
        'students': [student.id for student in students]
    }
    course_id = courses[0].id
    response = client.patch(f'/api/v1/courses/{course_id}/', data=data, format='json')

    assert response.status_code == 200
    response = response.json()
    assert response['name'] == 'UPDATED NAME'

    assert response['students'] == [student.id for student in students]


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    courses = courses_factory(_quantity=10)

    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 204


@pytest.mark.parametrize(
    ['max'], (
            ('20',),
            ('50',),
            ('100',)
    )
)
@pytest.mark.django_db
def test_max_students_in_course(client, student_factory, max, settings):
    students = student_factory(_quantity=20)
    settings.MAX_STUDENTS_PER_COURSE = int(max)
    data = {
        'name': 'TEST',
        'students': [student.id for student in students]
    }
    response = client.post('/api/v1/courses/', data=data, format='json')
    assert response.status_code == 201

    response = response.json()

    assert response['name'] == "TEST"
    assert len(response['students']) <= 20


@pytest.mark.parametrize(
    ['max'], (
            ('19',),
            ('1',)
    )
)
@pytest.mark.django_db
def test_too_much_students_course(client, student_factory, max, settings):
    students = student_factory(_quantity=20)
    settings.MAX_STUDENTS_PER_COURSE = int(max)
    data = {
        'name': 'TEST',
        'students': [student.id for student in students]
    }
    response = client.post('/api/v1/courses/', data=data, format='json')
    assert not response.status_code == 201
