<template>
  <div class="about">
    <v-card flat class="ma-5 pa-5" >
      <h1>1. Общие сведения о программе</h1>
      <h3>
          1.1	Назначение программного комплекса
        
      </h3>
      <span style="font-size: 18px;">
          Программный комплекс «ОКО-ВКА» предназначен для выявления в военнослужащих ИГ на основе данных социальных сетей.
      </span>
      <h3>
          1.2	Описание функциональных возможностей программного комплекса
          <br>
      </h3>
      <span style="font-size: 18px;">
           ПК «ОКО-ВКА» предоставляет пользователям следующие функциональные возможности.
          <br>
          1)	Возможность работы с данными социальных сетей (Вконтакте, Facebook, Strava):
          <br>
          а.	сбор информации из социальных сетей;
          <br>
          б.	предобработка получаемой информации;
          <br>
          в.	сохранение данных в БД PostgreSQL;
          <br>
          г.	редактирование данных в БД PostgreSQL.
          <br>
          2)	Возможность работы с отчетными информационными документами (далее ОИД):
          <br>
          а.	формирование ОИД;
          <br>
          б.	редактирование ОИД;
          <br>
          в.	визуализация ОИД;
          <br>
          г.	выгрузка ОИД в форматe XLSX.
          <br>
          3)	Возможность сбора информации в заданном географическом районе (точка, полигон)
          <br>
          4)	Возможность ведения информационного мониторинга заданных источников информации в автоматизированном режиме. 
          <br>
      </span>
      <h3>
          1.3	Сведения о технических и программных средствах, обеспечивающих выполнение программы
      </h3>
      <span style="font-size: 18px;">
        Рекомендуемая конфигурация ПК, на котором разворачивается система:
        <br>
        - тип процессора – Intel Core i7;
        <br>
        - объем оперативного запоминающего устройства – 16 Гб;
        <br> 
        - тип видеокарты – NVIDIA GeForce GTX 1660.;
        <br>
        - тактовая частота процессора: не менее 2 GHz. Dual Core;
        <br>
        - не менее 8 (восьми) портов 1 Gigabit Ethernet;
        <br>
        - совместимость с Комплектом ПО управления базами данных. Совместимость должна быть подтверждена производителем ПО;
        <br>
        - жесткий диск объемом не менее 1 Тб;
        <br>
        - наличие не менее двух видеовыходов;
        <br>
        - источник бесперебойного электропитания – не менее 750VA/500W.
        <br>
      </span>
      <br>
      <h1>
        2. Перечень инструкций-команд по работе с программным комплексом «ОКО-ВКА»
      </h1>
      <h3>Инструкция №1. Подключение к удаленной рабочей станции.</h3>
      <span style="font-size: 18px;">
          а.	Запустите консоль bash.
          <br>
          б.	Подключитесь к рабочей станции по протоколу ssh выполнив команду:
          ssh root@ip 
          где, «root» - имя пользователя, «ip» - IP адрес удаленной рабочей станции
      </span>
      <h3>Инструкция №2. Настройка окружения ПК «ОКО-ВКА».</h3>
      <span style="font-size: 18px;">
          а.	Убедитесь в наличии подключения к удаленной рабочей станции.
          <br>
          б.	 Загрузите репозиторий с исходным кодом программного комплекса «ОКО-ВКА»
          <br>
          в.	Перейдите в загруженную папку и запустите сборку окружения командой:
          cd папка/
          docker-compose build
      </span>
      <h3>Инструкция №3. Запуск ПК «ОКО-ВКА».</h3>
      <span style="font-size: 18px;">
          а.	Убедитесь в наличии подключения к удаленной рабочей станции.
          <br>
          б.	Убедитесь, что окружение для работы настроено. 
          <br>
          в.	Запустите программный комплекс командой:
          docker-compose up
      </span>
      <h3>
          Инструкция №4. Завершение работы ПК «ОКО-ВКА».
      </h3>
      <span style="font-size: 18px;">
          а.	Убедитесь в наличии подключения к удаленной рабочей станции.
          <br>
          б.	Убедитесь, что ПК «ОКО-ВКА» - запущен. 
          <br>
          в.	Для остановки программного комплекса выполните команду:
          docker-compose down
      </span>
      <h3>
          Инструкция №5. Обновление ПК «ОКО-ВКА».
      </h3>
      <span style="font-size: 18px;">
          а.	Убедитесь в наличии подключения к удаленной рабочей станции.
          <br>
          б.	Убедитесь, что окружение для работы настроено. 
          <br>
          в.	Обновите программный комплекс командой в консоли bash:
          git pull
          docker-compose restart
      </span>
      













    </v-card>
  </div>
</template>
