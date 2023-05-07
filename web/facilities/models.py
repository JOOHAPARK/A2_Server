from django.db import models


class Cafe(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cafe'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Convenience(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'convenience'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Gym(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gym'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Hair(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hair'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Hospital(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hospital'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Laundry(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'laundry'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Mart(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mart'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)


class Pharmacy(models.Model):
    opnsfteamcode = models.CharField(db_column='opnSfTeamCode', primary_key=True, max_length=7)  # Field name made lowercase. The composite primary key (opnSfTeamCode, mgtNo, opnSvcId) found, that is not supported. The first column is selected.
    mgtno = models.CharField(db_column='mgtNo', max_length=40)  # Field name made lowercase.
    opnsvcid = models.CharField(db_column='opnSvcId', max_length=10)  # Field name made lowercase.
    updategbn = models.CharField(db_column='updateGbn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='updateDt', blank=True, null=True)  # Field name made lowercase.
    bplcnm = models.CharField(db_column='bplcNm', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sitepostno = models.CharField(db_column='sitePostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sitewhladdr = models.CharField(db_column='siteWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rdnpostno = models.CharField(db_column='rdnPostNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    rdnwhladdr = models.CharField(db_column='rdnWhlAddr', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trdstategbn = models.CharField(db_column='trdStateGbn', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dtlstategbn = models.CharField(db_column='dtlStateGbn', max_length=4, blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(max_length=20, blank=True, null=True)
    y = models.CharField(max_length=20, blank=True, null=True)
    lastmodts = models.DateTimeField(db_column='lastModTs', blank=True, null=True)  # Field name made lowercase.
    uptaenm = models.CharField(db_column='uptaeNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pharmacy'
        unique_together = (('opnsfteamcode', 'mgtno', 'opnsvcid'),)